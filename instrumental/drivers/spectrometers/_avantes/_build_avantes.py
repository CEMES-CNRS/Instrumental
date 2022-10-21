#_build_thorlabs tlpm lib for powermeter using the tlpm library
# written by Sébastien Weber
# 2021/11/29


from nicelib import build_lib, generate_bindings
from nicelib.process import declspec_hook, struct_func_hook, stdcall_hook, cdecl_hook, extern_c_hook, modify_pattern, remove_pattern
import os


header_info = {
        'win*': {
            'path': (
                r'C:\ProgramData\avantes\AS5216x64-DLL_2.3\examples\Qtdemos\Qtdemo_simple_demo',
            ),
            'header': 'as5216.h'
        },
}

lib_names = {
    'win*:64': ('as5216x64',),
}



def dll_api_hook(tokens):
    return modify_pattern(tokens, [('d', 'extern'), ('d', '"C"'), ('d', '__declspec'),
                                   ])

def rm_dllapi_hook(tokens):
    return remove_pattern(tokens, ['extern', '"C"', '__declspec', '(',  'dllexport', ')'])

def rm_const_hook(tokens):
    return remove_pattern(tokens, ['const'])

preamble = """
"""

def build():
    build_lib(header_info, lib_names, '_avanteslib', __file__, preamble=preamble,
              ignore_system_headers=True,
              ignored_headers=[],
              token_hooks=(rm_dllapi_hook),
              override=True)


# def bindings():
#     with open('bindings.py') as f:
#         generate_bindings(header_info, f)


if __name__ == '__main__':
    build()
    #bindings()