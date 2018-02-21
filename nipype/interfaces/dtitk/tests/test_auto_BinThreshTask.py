# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import BinThreshTask


def test_BinThreshTask_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            exists=True,
            mandatory=False,
            position=0,
        ),
        in_numbers=dict(
            argstr='%s',
            exists=True,
            mandatory=False,
            position=2,
        ),
        out_file=dict(
            argstr='%s',
            exists=True,
            mandatory=False,
            position=1,
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = BinThreshTask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_BinThreshTask_outputs():
    output_map = dict(out_file=dict(), )
    outputs = BinThreshTask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
