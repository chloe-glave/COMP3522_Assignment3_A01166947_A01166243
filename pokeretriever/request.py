class Request:

    def __init__(self, mode: str, input_file, output_file, is_expanded: bool = False):
        self.mode = mode
        self.input_file = input_file
        self.is_expanded = is_expanded
        self.output_file = output_file
