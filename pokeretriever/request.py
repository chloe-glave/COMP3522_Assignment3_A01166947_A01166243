import argparse


class Request:

    def __init__(self):
        self.mode = None
        self.input_file = None
        self.input_data = None
        self.is_expanded = False
        self.output_file = None
        self.setup_request_commandline()

    def setup_request_commandline(self):
        """
        Implements the argparse module to accept arguments via the command
        line. This function specifies what these arguments are and
        updates the Request's instance variables accordingly.
        If something goes wrong with provided arguments then the function prints an error message and
        exits the application.
        :return: None
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("mode",
                            help="The mode that the pokedex will be opened in. Must be one of 'pokemon',"
                                 "'ability' or 'move'.")

        input_group = parser.add_mutually_exclusive_group()
        input_group.add_argument("-f", "--inputfile",
                           help="File to input data from, must end in '.txt'.")
        input_group.add_argument("-d", "--inputdata",
                                 help="Data to request from the pokedex, must be int or string. Ex. name of a"
                                      "pokemon or numeric ID of an ability.")

        parser.add_argument("-e", "--expanded", action="store_true",
                            help="Optional argument, runs pokedex in expanded mode (more detailed information given).")
        parser.add_argument("-o", "--output",
                            help="File name to print query result(s) to, must end with '.txt'. If unspecified,"
                                 "output will be printed to the console.")

        try:
            args = parser.parse_args()
            self.mode = args.mode
            self.input_file = args.inputfile
            self.input_data = args.inputdata
            self.is_expanded = args.expanded
            self.output_file = args.output

        except Exception as e:
            print(f"Error! Could not read arguments.\n{e}")
            quit()

    def __str__(self):
        return f"Request:\n" \
               f"Mode {self.mode}\n" \
               f"Input file {self.input_file}\n" \
               f"Input data {self.input_data}\n" \
               f"Is expanded? {self.is_expanded}\n" \
               f"Output file {self.output_file}"


if __name__ == '__main__':  # run this file with args to test arg parsing
    req = Request()
    print(req)
