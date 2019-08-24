import os

import requests

patches = {
    'cEP': {'001': ['https://github.com/coala/cEPs/pull/180.patch',
                    'coala-enhancement-proposal-for-support-toml-project.patch']},
    'coala': {'001': ['https://github.com/coala/coala/pull/6027.patch',
                      'TomlConfParser-and-loading-system-for-running-toml-files.patch'],
              '002': ['https://github.com/coala/coala/pull/6032.patch',
                      'Langauge-definition-for-TOML.patch'],
              '003': ['https://github.com/coala/coala/pull/6043.patch',
                      'TomlConfWriter-and-ConfigConverter.patch'],
              '004': ['https://github.com/coala/coala/pull/6049.patch',
                      'ConfigGenerator-for-generating-coafiles.patch']
              },
    'coala-documentation': {

        '001': ['https://github.com/coala/documentation/pull/598.patch',
                'Documentation-on-writing-configuration-files-in-TOML.patch'],
        '002': ['https://github.com/coala/documentation/pull/599.patch',
                'Documentation-on-using-ConfigGenerator.patch']

    },

    'coala-quickstart': {
        '001': ['https://github.com/coala/coala-quickstart/pull/335.patch',
                'Support-coala-quickstart-to-generate-config-files-in-TOML.patch']
    },

    'coala-antlr': {
        '001': ['https://gitlab.com/coala/bears/coala-antlr/merge_requests/46.patch',
                'A-set-of-bears-for-linting-TOML-files.patch']
    },

    'coala-mobans': {
        '001': ['https://gitlab.com/coala/mobans/merge_requests/136.patch',
                'coala-setup.py.jj2-Add-system_coafile.patch']
    },

    'toml': {
        '001': ['https://github.com/uiri/toml/commit/7963467bc3ac9c9834d33d303efb4fdb94858b38.patch',
                'Support-for-toml-library-to-store-comments.patch']
    },

    'coala-styles':{
        '001': ['https://github.com/PrajwalM2212/coala-styles/commit/069d088516be25dc2e6d093bb9fec014698b34f9.patch',
                'Repository-for-style-guide-configurations.patch']
    }

}

main_folder = 'gsoc_patches'


def download_cached_file(url, filename):
    response = requests.get(url, stream=True, timeout=20)
    response.raise_for_status()

    with open(filename, 'ab') as file:
        for chunk in response.iter_content(125):
            file.write(chunk)


if __name__ == '__main__':
    import time
    import logging

    main_dir = os.path.join(os.path.abspath(os.getcwd()), main_folder)
    os.mkdir(main_dir)
    d = {}
    for name, d in patches.items():
        dir_name = os.path.join(main_dir, name)
        os.mkdir(dir_name)
        for num, lst in d.items():
            download_cached_file(lst[0], os.path.join(dir_name, num + '-' + lst[1]))
            logging.info('Downloaded {} as {}'.format(lst[0], lst[1]))
            time.sleep(3)


