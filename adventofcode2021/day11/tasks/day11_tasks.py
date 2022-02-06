import logging # https://docs.python.org/3/howto/logging.html
import sys
import os.path
import numpy as np

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

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
    def calc(self):
        return sum([chunk.get_score() for chunk in self.line_chunks])
    def calc_complex(self) -> int:
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


