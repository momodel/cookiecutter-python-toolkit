import os
import sys

# sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.dirname(__file__))


class {{cookiecutter.module_name}}(object):

    def __init__(self, input={}):
        '''

        :param input:
        '''
        self.checkpoint_dir = os.path.dirname(__file__) + "/checkpoint"
        pass

    def run(self, input={}):
        '''

        :param input:
        :return:
        '''
        pass


if __name__ == '__main__':
    func_name = sys.argv[0]
    instance = {{cookiecutter.module_name}}()
    getattr(instance, func_name)()
