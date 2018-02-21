# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import MakeSurfaces


def test_MakeSurfaces_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        copy_inputs=dict(),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fix_mtl=dict(argstr='-fix_mtl', ),
        hemisphere=dict(
            argstr='%s',
            mandatory=True,
            position=-1,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_T1=dict(argstr='-T1 %s', ),
        in_aseg=dict(argstr='-aseg %s', ),
        in_filled=dict(mandatory=True, ),
        in_label=dict(xor=['noaparc'], ),
        in_orig=dict(
            argstr='-orig %s',
            mandatory=True,
        ),
        in_white=dict(),
        in_wm=dict(mandatory=True, ),
        longitudinal=dict(argstr='-long', ),
        maximum=dict(argstr='-max %.1f', ),
        mgz=dict(argstr='-mgz', ),
        no_white=dict(argstr='-nowhite', ),
        noaparc=dict(
            argstr='-noaparc',
            xor=['in_label'],
        ),
        orig_pial=dict(
            argstr='-orig_pial %s',
            requires=['in_label'],
        ),
        orig_white=dict(argstr='-orig_white %s', ),
        subject_id=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
            usedefault=True,
        ),
        subjects_dir=dict(),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        white=dict(argstr='-white %s', ),
        white_only=dict(argstr='-whiteonly', ),
    )
    inputs = MakeSurfaces.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_MakeSurfaces_outputs():
    output_map = dict(
        out_area=dict(),
        out_cortex=dict(),
        out_curv=dict(),
        out_pial=dict(),
        out_thickness=dict(),
        out_white=dict(),
    )
    outputs = MakeSurfaces.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
