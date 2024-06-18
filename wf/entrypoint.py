from dataclasses import dataclass
from enum import Enum
import os
import subprocess
import requests
import shutil
from pathlib import Path
import typing
import typing_extensions

from latch.resources.workflow import workflow
from latch.resources.tasks import nextflow_runtime_task, custom_task
from latch.types.file import LatchFile
from latch.types.directory import LatchDir, LatchOutputDir
from latch.ldata.path import LPath
from latch_cli.nextflow.workflow import get_flag
from latch_cli.nextflow.utils import _get_execution_name
from latch_cli.utils import urljoins
from latch.types import metadata
from flytekit.core.annotation import FlyteAnnotation

from latch_cli.services.register.utils import import_module_by_path

meta = Path("latch_metadata") / "__init__.py"
import_module_by_path(meta)
import latch_metadata

@custom_task(cpu=0.25, memory=0.5, storage_gib=1)
def initialize() -> str:
    token = os.environ.get("FLYTE_INTERNAL_EXECUTION_ID")
    if token is None:
        raise RuntimeError("failed to get execution token")

    headers = {"Authorization": f"Latch-Execution-Token {token}"}

    print("Provisioning shared storage volume... ", end="")
    resp = requests.post(
        "http://nf-dispatcher-service.flyte.svc.cluster.local/provision-storage",
        headers=headers,
        json={
            "storage_gib": 100,
        }
    )
    resp.raise_for_status()
    print("Done.")

    return resp.json()["name"]






@nextflow_runtime_task(cpu=4, memory=8, storage_gib=100)
def nextflow_runtime(pvc_name: str, input: LatchFile, anchor_peaks: typing.Optional[LatchFile], outdir: typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})], email: typing.Optional[str], multiqc_title: typing.Optional[str], genome: typing.Optional[str], fasta: typing.Optional[LatchFile], bwa_index: typing.Optional[str], gtf: typing.Optional[LatchFile], gff: typing.Optional[LatchFile], gene_bed: typing.Optional[LatchFile], mappability: typing.Optional[LatchFile], macs_gsize: typing.Optional[str], ucscname: typing.Optional[str], blacklist: typing.Optional[LatchFile], publish_mappability: typing.Optional[bool], publish_genome: typing.Optional[bool], call_high_peak: typing.Optional[bool], multiqc_methods_description: typing.Optional[str], skip_cutadapt: typing.Optional[bool], resample_pairs: typing.Optional[bool], skip_fastqc: typing.Optional[bool], skip_peak_annotation: typing.Optional[bool], skip_diff_analysis: typing.Optional[bool], skip_multiqc: typing.Optional[bool], do_apa: typing.Optional[bool], skip_compartments: typing.Optional[bool], skip_tads: typing.Optional[bool], skip_interactions: typing.Optional[bool], do_tfea: typing.Optional[bool], create_virtual_4c: typing.Optional[bool], skip_circos: typing.Optional[bool], method: typing.Optional[str], enzyme: typing.Optional[str], restriction_sites_cut_off: typing.Optional[float], cutadapt_5end: typing.Optional[str], shiftsize: typing.Optional[int], smooth_window: typing.Optional[int], qval_thresh: typing.Optional[float], cool_bin: typing.Optional[str], maps_digest_file: typing.Optional[str], maps_cutoff_counts: typing.Optional[int], maps_cutoff_fold_change: typing.Optional[float], maps_cutoff_fdr: typing.Optional[float], maps_filter: typing.Optional[str], maps_model: typing.Optional[str], snow_type: typing.Optional[str], hicdcplus_cutoff_fdr: typing.Optional[float], peakachu_pretrained_url: typing.Optional[str], r1_pval_thresh: typing.Optional[float], res_compartments: typing.Optional[int], res_tads: typing.Optional[int], tad_tool: typing.Optional[str], apa_peak: typing.Optional[str], apa_tool: typing.Optional[str], apa_format: typing.Optional[str], compartments_tool: typing.Optional[str], interactions_tool: typing.Optional[str], da_tool: typing.Optional[str], v4c_tool: typing.Optional[str], tfea_tool: typing.Optional[str], juicer_tools_jar: typing.Optional[str], juicer_norm_method: typing.Optional[str], peak_interactions_threshold: typing.Optional[int], v4c_max_events: typing.Optional[int], hic_tools_jar: typing.Optional[str]) -> None:
    try:
        shared_dir = Path("/nf-workdir")



        ignore_list = [
            "latch",
            ".latch",
            "nextflow",
            ".nextflow",
            "work",
            "results",
            "miniconda",
            "anaconda3",
            "mambaforge",
        ]

        shutil.copytree(
            Path("/root"),
            shared_dir,
            ignore=lambda src, names: ignore_list,
            ignore_dangling_symlinks=True,
            dirs_exist_ok=True,
        )

        cmd = [
            "/root/nextflow",
            "run",
            str(shared_dir / "main.nf"),
            "-work-dir",
            str(shared_dir),
            "-profile",
            "docker",
            "-c",
            "latch.config",
                *get_flag('input', input),
                *get_flag('method', method),
                *get_flag('anchor_peaks', anchor_peaks),
                *get_flag('outdir', outdir),
                *get_flag('email', email),
                *get_flag('multiqc_title', multiqc_title),
                *get_flag('genome', genome),
                *get_flag('fasta', fasta),
                *get_flag('bwa_index', bwa_index),
                *get_flag('gtf', gtf),
                *get_flag('gff', gff),
                *get_flag('gene_bed', gene_bed),
                *get_flag('mappability', mappability),
                *get_flag('macs_gsize', macs_gsize),
                *get_flag('ucscname', ucscname),
                *get_flag('blacklist', blacklist),
                *get_flag('publish_mappability', publish_mappability),
                *get_flag('publish_genome', publish_genome),
                *get_flag('enzyme', enzyme),
                *get_flag('restriction_sites_cut_off', restriction_sites_cut_off),
                *get_flag('cutadapt_5end', cutadapt_5end),
                *get_flag('shiftsize', shiftsize),
                *get_flag('smooth_window', smooth_window),
                *get_flag('qval_thresh', qval_thresh),
                *get_flag('cool_bin', cool_bin),
                *get_flag('maps_digest_file', maps_digest_file),
                *get_flag('maps_cutoff_counts', maps_cutoff_counts),
                *get_flag('maps_cutoff_fold_change', maps_cutoff_fold_change),
                *get_flag('maps_cutoff_fdr', maps_cutoff_fdr),
                *get_flag('maps_filter', maps_filter),
                *get_flag('maps_model', maps_model),
                *get_flag('snow_type', snow_type),
                *get_flag('hicdcplus_cutoff_fdr', hicdcplus_cutoff_fdr),
                *get_flag('peakachu_pretrained_url', peakachu_pretrained_url),
                *get_flag('call_high_peak', call_high_peak),
                *get_flag('r1_pval_thresh', r1_pval_thresh),
                *get_flag('res_compartments', res_compartments),
                *get_flag('res_tads', res_tads),
                *get_flag('tad_tool', tad_tool),
                *get_flag('apa_peak', apa_peak),
                *get_flag('apa_tool', apa_tool),
                *get_flag('apa_format', apa_format),
                *get_flag('compartments_tool', compartments_tool),
                *get_flag('interactions_tool', interactions_tool),
                *get_flag('da_tool', da_tool),
                *get_flag('v4c_tool', v4c_tool),
                *get_flag('tfea_tool', tfea_tool),
                *get_flag('juicer_tools_jar', juicer_tools_jar),
                *get_flag('juicer_norm_method', juicer_norm_method),
                *get_flag('peak_interactions_threshold', peak_interactions_threshold),
                *get_flag('v4c_max_events', v4c_max_events),
                *get_flag('hic_tools_jar', hic_tools_jar),
                *get_flag('multiqc_methods_description', multiqc_methods_description),
                *get_flag('skip_cutadapt', skip_cutadapt),
                *get_flag('resample_pairs', resample_pairs),
                *get_flag('skip_fastqc', skip_fastqc),
                *get_flag('skip_peak_annotation', skip_peak_annotation),
                *get_flag('skip_diff_analysis', skip_diff_analysis),
                *get_flag('skip_multiqc', skip_multiqc),
                *get_flag('do_apa', do_apa),
                *get_flag('skip_compartments', skip_compartments),
                *get_flag('skip_tads', skip_tads),
                *get_flag('skip_interactions', skip_interactions),
                *get_flag('do_tfea', do_tfea),
                *get_flag('create_virtual_4c', create_virtual_4c),
                *get_flag('skip_circos', skip_circos)
        ]

        print("Launching Nextflow Runtime")
        print(' '.join(cmd))
        print(flush=True)

        env = {
            **os.environ,
            "NXF_HOME": "/root/.nextflow",
            "NXF_OPTS": "-Xms2048M -Xmx8G -XX:ActiveProcessorCount=4",
            "K8S_STORAGE_CLAIM_NAME": pvc_name,
            "NXF_DISABLE_CHECK_LATEST": "true",
        }
        subprocess.run(
            cmd,
            env=env,
            check=True,
            cwd=str(shared_dir),
        )
    finally:
        print()

        nextflow_log = shared_dir / ".nextflow.log"
        if nextflow_log.exists():
            name = _get_execution_name()
            if name is None:
                print("Skipping logs upload, failed to get execution name")
            else:
                remote = LPath(urljoins("latch:///your_log_dir/nf_nf_core_hicar", name, "nextflow.log"))
                print(f"Uploading .nextflow.log to {remote.path}")
                remote.upload_from(nextflow_log)



@workflow(metadata._nextflow_metadata)
def nf_nf_core_hicar(input: LatchFile, anchor_peaks: typing.Optional[LatchFile], outdir: typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})], email: typing.Optional[str], multiqc_title: typing.Optional[str], genome: typing.Optional[str], fasta: typing.Optional[LatchFile], bwa_index: typing.Optional[str], gtf: typing.Optional[LatchFile], gff: typing.Optional[LatchFile], gene_bed: typing.Optional[LatchFile], mappability: typing.Optional[LatchFile], macs_gsize: typing.Optional[str], ucscname: typing.Optional[str], blacklist: typing.Optional[LatchFile], publish_mappability: typing.Optional[bool], publish_genome: typing.Optional[bool], call_high_peak: typing.Optional[bool], multiqc_methods_description: typing.Optional[str], skip_cutadapt: typing.Optional[bool], resample_pairs: typing.Optional[bool], skip_fastqc: typing.Optional[bool], skip_peak_annotation: typing.Optional[bool], skip_diff_analysis: typing.Optional[bool], skip_multiqc: typing.Optional[bool], do_apa: typing.Optional[bool], skip_compartments: typing.Optional[bool], skip_tads: typing.Optional[bool], skip_interactions: typing.Optional[bool], do_tfea: typing.Optional[bool], create_virtual_4c: typing.Optional[bool], skip_circos: typing.Optional[bool], method: typing.Optional[str] = 'HiCAR', enzyme: typing.Optional[str] = 'CviQI', restriction_sites_cut_off: typing.Optional[float] = 0.5, cutadapt_5end: typing.Optional[str] = '^TAC', shiftsize: typing.Optional[int] = -75, smooth_window: typing.Optional[int] = 150, qval_thresh: typing.Optional[float] = 0.01, cool_bin: typing.Optional[str] = '5000_10000', maps_digest_file: typing.Optional[str] = 'None', maps_cutoff_counts: typing.Optional[int] = 12, maps_cutoff_fold_change: typing.Optional[float] = 2.0, maps_cutoff_fdr: typing.Optional[float] = 2.0, maps_filter: typing.Optional[str] = 'None', maps_model: typing.Optional[str] = 'pospoisson', snow_type: typing.Optional[str] = 'SOCK', hicdcplus_cutoff_fdr: typing.Optional[float] = 0.05, peakachu_pretrained_url: typing.Optional[str] = 'http://3dgenome.fsm.northwestern.edu/peakachu/HiCAR-models/HiCAR-peakachu-pretrained.', r1_pval_thresh: typing.Optional[float] = 0.1, res_compartments: typing.Optional[int] = 100000, res_tads: typing.Optional[int] = 10000, tad_tool: typing.Optional[str] = 'hicexplorer', apa_peak: typing.Optional[str] = 'Anchor 1D peaks', apa_tool: typing.Optional[str] = 'hicexplorer', apa_format: typing.Optional[str] = 'png', compartments_tool: typing.Optional[str] = 'cooltools', interactions_tool: typing.Optional[str] = 'maps', da_tool: typing.Optional[str] = 'diffhic', v4c_tool: typing.Optional[str] = 'hicexplorer', tfea_tool: typing.Optional[str] = 'homer', juicer_tools_jar: typing.Optional[str] = 'https://github.com/aidenlab/JuicerTools/releases/download/v3.0.0/juicer_tools.3.0.0.jar', juicer_norm_method: typing.Optional[str] = 'SCALE', peak_interactions_threshold: typing.Optional[int] = 2, v4c_max_events: typing.Optional[int] = 25, hic_tools_jar: typing.Optional[str] = 'https://github.com/aidenlab/HiCTools/releases/download/v3.30.00/hic_tools.3.30.00.jar') -> None:
    """
    nf-core/hicar

    Sample Description
    """

    pvc_name: str = initialize()
    nextflow_runtime(pvc_name=pvc_name, input=input, method=method, anchor_peaks=anchor_peaks, outdir=outdir, email=email, multiqc_title=multiqc_title, genome=genome, fasta=fasta, bwa_index=bwa_index, gtf=gtf, gff=gff, gene_bed=gene_bed, mappability=mappability, macs_gsize=macs_gsize, ucscname=ucscname, blacklist=blacklist, publish_mappability=publish_mappability, publish_genome=publish_genome, enzyme=enzyme, restriction_sites_cut_off=restriction_sites_cut_off, cutadapt_5end=cutadapt_5end, shiftsize=shiftsize, smooth_window=smooth_window, qval_thresh=qval_thresh, cool_bin=cool_bin, maps_digest_file=maps_digest_file, maps_cutoff_counts=maps_cutoff_counts, maps_cutoff_fold_change=maps_cutoff_fold_change, maps_cutoff_fdr=maps_cutoff_fdr, maps_filter=maps_filter, maps_model=maps_model, snow_type=snow_type, hicdcplus_cutoff_fdr=hicdcplus_cutoff_fdr, peakachu_pretrained_url=peakachu_pretrained_url, call_high_peak=call_high_peak, r1_pval_thresh=r1_pval_thresh, res_compartments=res_compartments, res_tads=res_tads, tad_tool=tad_tool, apa_peak=apa_peak, apa_tool=apa_tool, apa_format=apa_format, compartments_tool=compartments_tool, interactions_tool=interactions_tool, da_tool=da_tool, v4c_tool=v4c_tool, tfea_tool=tfea_tool, juicer_tools_jar=juicer_tools_jar, juicer_norm_method=juicer_norm_method, peak_interactions_threshold=peak_interactions_threshold, v4c_max_events=v4c_max_events, hic_tools_jar=hic_tools_jar, multiqc_methods_description=multiqc_methods_description, skip_cutadapt=skip_cutadapt, resample_pairs=resample_pairs, skip_fastqc=skip_fastqc, skip_peak_annotation=skip_peak_annotation, skip_diff_analysis=skip_diff_analysis, skip_multiqc=skip_multiqc, do_apa=do_apa, skip_compartments=skip_compartments, skip_tads=skip_tads, skip_interactions=skip_interactions, do_tfea=do_tfea, create_virtual_4c=create_virtual_4c, skip_circos=skip_circos)

