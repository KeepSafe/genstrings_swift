import argparse
import re
import io
import os
from collections import namedtuple, OrderedDict

OUTPUT_FILE = 'Localizable.strings'
OUTPUT_ENCODING = 'utf-16'
OUTPUT_LINE_PATTERN = u'/* {comment} */\n"{key}" = "{value}";\n\n'

pattern = re.compile('/\* ([^"]*) \*/\s"([^"]*)" = "([^"]*)";')
String = namedtuple('String', ['key', 'value', 'comment'])


def read_cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='Command output directory', default='.')
    parser.add_argument('filepaths', nargs='+', help='files to merge')
    args = parser.parse_args()
    return args


def generate_strings(filepaths):
    all_strings = []
    for filepath in filepaths:
        strings = parse_file(filepath)
        all_strings.extend(strings)

    unique_strings = OrderedDict(map(lambda s: (s.key, s), all_strings))
    return unique_strings.values()


def parse_file(filepath):
    strings = []
    with io.open(filepath, encoding=OUTPUT_ENCODING) as fp:
        content = fp.read()
        for match in pattern.finditer(content):
            comment = match.group(1)
            key = match.group(2)
            value = match.group(3)
            string = String(key, value, comment)
            strings.append(string)
    return strings


def save_strings(output_dir, strings):
    filepath = os.path.join(output_dir, OUTPUT_FILE)
    with io.open(filepath, 'w', encoding=OUTPUT_ENCODING) as fp:
        output_lines = map(lambda s: OUTPUT_LINE_PATTERN.format(**s._asdict()), strings)
        fp.writelines(output_lines)


def main():
    args = read_cmd()
    strings = generate_strings(args.filepaths)
    save_strings(args.output, strings)


if __name__ == '__main__':
    main()
