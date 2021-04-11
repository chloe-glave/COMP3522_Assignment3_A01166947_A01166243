import argparse

class Request:

    # mode: str, input_file, output_file, is_expanded: bool = False
    def __init__(self):
        self.mode = None
        self.input_file = None
        self.output_file = None
        self.is_expanded = False
        self.setup_request_commandline()

    def setup_request_commandline(self):
        """
        Implements the argparse module to accept arguments via the command
        line. This function specifies what these arguments are and parses it
        into an object of type Request. If something goes wrong with
        provided arguments then the function prints an error message and
        exits the application.
        :return: The object of type Request with all the arguments provided
        in it.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("mode",
                            help="The mode that the pokedex will be opened in. Must be one of 'pokemon',"
                                 "'ability' or 'move'.")

        group = parser.add_mutually_exclusive_group()
        group.add_argument("-f", "--inputfile", )

        # parser.add_argument("key", help="The key to use when encrypting or "
        #                                 "decrypting. This needs to be of "
        #                                 "length 8, 16 or 24")
        # parser.add_argument("-s", "--string", help="The string that needs to be "
        #                                            "encrypted or decrypted")
        # parser.add_argument("-f", "--file", help="The text file that needs to be"
        #                                          "encrypted or decrypted")
        # parser.add_argument("-o", "--output", default="print",
        #                     help="The output of the program. This is 'print' by "
        #                          "default, but can be set to a file name as well.")
        # parser.add_argument("-m", "--mode", default="en",
        #                     help="The mode to run the program in. If 'en' (default)"
        #                          " then the program will encrypt, 'de' will cause "
        #                          "the program to decrypt")
        try:
            args = parser.parse_args()
            self.mode = args.mode
        except Exception as e:
            print(f"Error! Could not read arguments.\n{e}")
            quit()


if __name__ == '__main__':
    print("start")
    req = Request()
    print(req.mode)
