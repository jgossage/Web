"""
Generator for template for HTML navigation

This script generates a Liquid template tht will result in the 'nav.html' file
that will define the navigation tree to be displayed in the navigation bar for
each web page that is displayed.
"""

import sys

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path
from typing import Any, cast, List, Optional, Sequence

__all__: List[Any] = []
__version__: str = '0.1'
__date__ = '2020-12-04'
__updated__ = '2020-12-04'

DEBUG = 0
TESTRUN = 0
PROFILE = 0


def run(args: Optional[Sequence[str]] = None) -> int:
    """Runs the actual script"""
    return 0


def main(argv: Optional[str] = None) -> int:  # IGNORE:C0111

    """Handle command line options."""

    if argv is None:
        argv = cast(str, sys.argv)
    else:
        sys.argv.extend(argv)

    program_name = Path(sys.argv[0]).stem
    program_version = f'v{__version__}'
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version,
                                                     program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split('\n')[1]
    program_license = f"""{program_shortdesc}
  Created by Jonathan Gossage on {str(__date__)}.
  Copyright 2020 Global Village. All rights reserved.
  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0
  Distributed on an 'AS IS' basis without warranties
  or conditions of any kind, either express or implied.
USAGE
"""

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license,
                                formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument('-v',
                            '--verbose',
                            dest='verbose',
                            action='count',
                            help='set verbosity level [default: %(default)s]')
        parser.add_argument('-V',
                            '--version',
                            action='version',
                            version=program_version_message)
        parser.add_argument('-c',
                            '--configuration',
                            dest='configuration')
        # Process arguments
        args = vars(parser.parse_args())

        # Load configuration

        run(cast(Optional[Sequence[str]], args))
        return 0
    except KeyboardInterrupt:
        # handle keyboard interrupt
        return 0
    except Exception as e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * ' '
        sys.stderr.write(f'{program_name}: {repr(e)}\n')
        sys.stderr.write(f'{indent}  for help use --help')
        return 2


if __name__ == '__main__':
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'scripts.generateModule_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open('profile_stats.txt', 'wb')
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())
