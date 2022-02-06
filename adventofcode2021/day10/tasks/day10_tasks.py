import logging # https://docs.python.org/3/howto/logging.html
import sys
import os.path
import numpy as np

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

SEPERATORS = {
    '-': {'start': '-', 'end': '-', 'points': 0, 'complete_points': 0},
    '{': {'start': '{', 'end': '}', 'points': 1197, 'complete_points': 3},
    '[': {'start': '[', 'end': ']', 'points': 57, 'complete_points': 2},
    '<': {'start': '<', 'end': '>', 'points': 25137, 'complete_points': 4},
    '(': {'start': '(', 'end': ')', 'points': 3, 'complete_points': 1}
    }

ILLIGAL = {
    '-': {'start': '-', 'end': '-', 'points': 0},
    '}': {'start': '{', 'end': '}', 'points': 1197},
    ']': {'start': '[', 'end': ']', 'points': 57},
    '>': {'start': '<', 'end': '>', 'points': 25137},
    ')': {'start': '(', 'end': ')', 'points': 3}
    }

INCOMPLETE = {
    '-': {'start': '-', 'end': '-', 'points': 0},
    '}': {'start': '{', 'end': '}', 'points': 3},
    ']': {'start': '[', 'end': ']', 'points': 2},
    '>': {'start': '<', 'end': '>', 'points': 4},
    ')': {'start': '(', 'end': ')', 'points': 1}
    }

class chunkObject(object):
    def __init__(self, character):
        self.start_character = character
        self.chunks = []
        self.corruption = []
        self.closed = False
        return None
    def add_chunk(self, chunk):
        self.chunks.append(chunk)
        return
    def close(self):
        if all([ch.is_closed() for ch in self.chunks]):
            self.closed = True
        else:
            RuntimeError('Cant close chunk')
        return None
    def is_closed(self):
        return self.closed
    def find_current_chunk(self):
        current_chunk = None
        for i, chunk in reversed(list(enumerate(self.chunks))):
            if chunk.is_closed() == False:
                current_chunk = chunk.find_current_chunk()
        if current_chunk == None:
            if self.is_closed() == True:
                current_chunk == None
            else:
                current_chunk = self
        return current_chunk
    def add_corruption(self, character):
        self.corruption.append(character)
        return None
    def get_corruption(self) -> int:
        score = 0
        if len(self.corruption) > 0:
            score += ILLIGAL[self.corruption[0]]['points']
        else:
            score += sum([ch.get_corruption() for ch in self.chunks])
        return score

    def process(self, character):
        current_chunk = self.find_current_chunk()
        if current_chunk.get_corruption() == 0:
            if character == SEPERATORS[current_chunk.start_character]['end']:
                current_chunk.close()
            else:
                if character in SEPERATORS.keys():
                    current_chunk.add_chunk(chunkObject(character))
                else:
                    logging.error('Chunk is corrupt, trying to process: ' + str(character))
                    current_chunk.add_corruption(character)
        return
    def get_score(self):
        current_chunk = self.find_current_chunk()
        return current_chunk.get_corruption()
    def get_completion_score(self) -> int:
        score:int = 0
        while self.is_closed() == False:
            current_chunk = self.find_current_chunk()
            if current_chunk.is_closed() == False:
                sep = SEPERATORS[current_chunk.start_character]
                current_chunk.close()
                score *= 5
                score += sep['complete_points']
            else:
                RuntimeError('Cant close chunk')
        return int(score/5)

class day10_tasks(object):
    """description of class"""

    def __init__(self, file: str) -> None:
        self.file = None
        self.line_segments = []
        full_file_path = DIR_PATH + '/'+ file
        self.line_chunks = []
        if (os.path.exists(full_file_path)):
            self.file = full_file_path
            file = None
            self.load()
        else:
            logging.error('file does not exist: ' + str(full_file_path))
            raise RuntimeError('file does not exist: ' + str(full_file_path))
        return

    def load(self) -> None:
        with open(self.file) as _f:
            self.lines = [line.strip() for line in _f.readlines()]
        
        for line in self.lines:
            lineChunk = chunkObject('-')
            for charactor in line:
                lineChunk.process(charactor)
            lineChunk.process('-')
            self.line_chunks.append(lineChunk)
        return
    def calc_syntax_error_score(self):
        return sum([chunk.get_score() for chunk in self.line_chunks])
    def calc_autocomplete_score(self) -> int:
        scores = []
        for chunk in self.line_chunks:
            if chunk.get_score() == 0:
                scores.append(chunk.get_completion_score())
        scores.sort()
        middle = int(scores[int((len(scores)-1)/2)])
        return middle

if __name__ == '__main__':
    file = 'resource/dataset_test.csv'
    run = day10_tasks(file)
    run.calc_syntax_error_score()
    run.calc_autocomplete_score()


