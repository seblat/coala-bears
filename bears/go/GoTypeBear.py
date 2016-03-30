from coalib.bearlib.abstractions.Linter import Linter


@Linter(executable='gotype',
        output_stream='stderr',
        output_format='regex',
        output_regex=r'.+:(?P<line>\d+):(?P<column>\d+): *(?P<message>.*)')
class GoTypeBear:
    """
    Checks the code using ``gotype``. This will run ``gotype`` over each file
    separately.
    """

    @staticmethod
    def create_arguments(filename, file, config_file):
        return '-e', filename
