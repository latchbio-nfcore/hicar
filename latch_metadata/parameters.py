
from dataclasses import dataclass
import typing
import typing_extensions

from flytekit.core.annotation import FlyteAnnotation

from latch.types.metadata import NextflowParameter
from latch.types.file import LatchFile
from latch.types.directory import LatchDir, LatchOutputDir

# Import these into your `__init__.py` file:
#
# from .parameters import generated_parameters

generated_parameters = {
    'input': NextflowParameter(
        type=LatchFile,
        default=None,
        section_title='Input/output options',
        description='Path to comma-separated file containing information about the samples in the experiment.',
    ),
    'method': NextflowParameter(
        type=typing.Optional[str],
        default='HiCAR',
        section_title=None,
        description='Metho for the experiment.',
    ),
    'anchor_peaks': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to anchor peaks',
    ),
    'outdir': NextflowParameter(
        type=typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})],
        default=None,
        section_title=None,
        description='The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure.',
    ),
    'email': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Email address for completion summary.',
    ),
    'multiqc_title': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='MultiQC report title. Printed as page header, used for filename if not otherwise specified.',
    ),
    'genome': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Reference genome options',
        description='Name of iGenomes reference.',
    ),
    'fasta': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to FASTA genome file.',
    ),
    'bwa_index': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Path to bwa index file.',
    ),
    'gtf': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to annotation gtf file.',
    ),
    'gff': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to annotation gff file.',
    ),
    'gene_bed': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to annotation gene bed file.',
    ),
    'mappability': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to genome mappability file.',
    ),
    'macs_gsize': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Effective genome size parameter required by MACS2.',
    ),
    'ucscname': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='UCSC assembly annotation name.',
    ),
    'blacklist': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to blacklist regions in BED format, used for filtering alignments.',
    ),
    'publish_mappability': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='publish mappability to results genome/mappability folder',
    ),
    'publish_genome': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='publish genome',
    ),
    'enzyme': NextflowParameter(
        type=typing.Optional[str],
        default='CviQI',
        section_title='Experiment design options',
        description='Specifies that the cutting position has to be using.',
    ),
    'restriction_sites_cut_off': NextflowParameter(
        type=typing.Optional[float],
        default=0.5,
        section_title=None,
        description='Specifies that the cutoff value used for mappability filter.',
    ),
    'cutadapt_5end': NextflowParameter(
        type=typing.Optional[str],
        default='^TAC',
        section_title=None,
        description="trim 5' end with the string if not skip_cutadapt",
    ),
    'shiftsize': NextflowParameter(
        type=typing.Optional[int],
        default=-75,
        section_title='MACS2 peak calling options',
        description='shift size for MACS2',
    ),
    'smooth_window': NextflowParameter(
        type=typing.Optional[int],
        default=150,
        section_title=None,
        description='extsize for MACS2',
    ),
    'qval_thresh': NextflowParameter(
        type=typing.Optional[float],
        default=0.01,
        section_title=None,
        description='cutoff qvalue',
    ),
    'cool_bin': NextflowParameter(
        type=typing.Optional[str],
        default='5000_10000',
        section_title='Interactions calling options',
        description='resolution bin size',
    ),
    'maps_digest_file': NextflowParameter(
        type=typing.Optional[str],
        default='None',
        section_title=None,
        description='output of restriction_cut_multipleenzyme.py.',
    ),
    'maps_cutoff_counts': NextflowParameter(
        type=typing.Optional[int],
        default=12,
        section_title=None,
        description='MAPS regression cutoff value',
    ),
    'maps_cutoff_fold_change': NextflowParameter(
        type=typing.Optional[float],
        default=2.0,
        section_title=None,
        description='MAPS regression fold change cutoff value',
    ),
    'maps_cutoff_fdr': NextflowParameter(
        type=typing.Optional[float],
        default=2.0,
        section_title=None,
        description='MAPS regression -log10(fdr) cutoff value',
    ),
    'maps_filter': NextflowParameter(
        type=typing.Optional[str],
        default='None',
        section_title=None,
        description='MAPS regression filter file name',
    ),
    'maps_model': NextflowParameter(
        type=typing.Optional[str],
        default='pospoisson',
        section_title=None,
        description='MAPS regression type',
    ),
    'snow_type': NextflowParameter(
        type=typing.Optional[str],
        default='SOCK',
        section_title=None,
        description='Type of snow cluster to use',
    ),
    'hicdcplus_cutoff_fdr': NextflowParameter(
        type=typing.Optional[float],
        default=0.05,
        section_title=None,
        description='FDR cutoff value',
    ),
    'peakachu_pretrained_url': NextflowParameter(
        type=typing.Optional[str],
        default='http://3dgenome.fsm.northwestern.edu/peakachu/HiCAR-models/HiCAR-peakachu-pretrained.',
        section_title=None,
        description='The predefined modle download prefix string',
    ),
    'call_high_peak': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Call high resolution peaks or not',
    ),
    'r1_pval_thresh': NextflowParameter(
        type=typing.Optional[float],
        default=0.1,
        section_title=None,
        description='cutoff pvalue for fragment (R1)',
    ),
    'res_compartments': NextflowParameter(
        type=typing.Optional[int],
        default=100000,
        section_title='Options related to compartment, TADs calling, and APA',
        description='The resolution for compartments calling',
    ),
    'res_tads': NextflowParameter(
        type=typing.Optional[int],
        default=10000,
        section_title=None,
        description='The resolution for TADs calling',
    ),
    'tad_tool': NextflowParameter(
        type=typing.Optional[str],
        default='hicexplorer',
        section_title=None,
        description="The caller for TADs, available choices: 'cooltools', 'hicexplorer', 'homer'",
    ),
    'apa_peak': NextflowParameter(
        type=typing.Optional[str],
        default='Anchor 1D peaks',
        section_title=None,
        description='The APA peak path',
    ),
    'apa_tool': NextflowParameter(
        type=typing.Optional[str],
        default='hicexplorer',
        section_title=None,
        description="APA tool, available choices: 'cooltools', 'hicexplorer', and 'juicebox'",
    ),
    'apa_format': NextflowParameter(
        type=typing.Optional[str],
        default='png',
        section_title=None,
        description='The APA output figure format. Currently this parameter will not affect the Juicer output format (always png format).',
    ),
    'compartments_tool': NextflowParameter(
        type=typing.Optional[str],
        default='cooltools',
        section_title=None,
        description="Call compartment tool, available choices: 'cooltools', 'hicexplorer', 'homer', and 'juicebox'",
    ),
    'interactions_tool': NextflowParameter(
        type=typing.Optional[str],
        default='maps',
        section_title=None,
        description="Call loops tool, available choices: 'maps', 'hicdcplus', and 'peakachu'",
    ),
    'da_tool': NextflowParameter(
        type=typing.Optional[str],
        default='diffhic',
        section_title=None,
        description="Differential analysis tool. Possible options are 'edger', 'diffhic', 'hicexplorer', and 'setOperation'",
    ),
    'v4c_tool': NextflowParameter(
        type=typing.Optional[str],
        default='hicexplorer',
        section_title=None,
        description="virtual 4c tool, available choices: 'cooltools', 'hicexplorer', and 'trackviewer'",
    ),
    'tfea_tool': NextflowParameter(
        type=typing.Optional[str],
        default='homer',
        section_title=None,
        description="Transcription Factor Enrichment Analysis tool, available choices: 'atacseqtfea', and 'homer'",
    ),
    'juicer_tools_jar': NextflowParameter(
        type=typing.Optional[str],
        default='https://github.com/aidenlab/JuicerTools/releases/download/v3.0.0/juicer_tools.3.0.0.jar',
        section_title=None,
        description='juicer_tools jar file url',
    ),
    'juicer_norm_method': NextflowParameter(
        type=typing.Optional[str],
        default='SCALE',
        section_title=None,
        description='Normalization methods',
    ),
    'peak_interactions_threshold': NextflowParameter(
        type=typing.Optional[int],
        default=2,
        section_title=None,
        description='parameter for HiCExplorer ChicSignificantinterations',
    ),
    'v4c_max_events': NextflowParameter(
        type=typing.Optional[int],
        default=25,
        section_title='Options related to tracks, HiCTools, and circos',
        description='max events to plot for virtual 4c',
    ),
    'hic_tools_jar': NextflowParameter(
        type=typing.Optional[str],
        default='https://github.com/aidenlab/HiCTools/releases/download/v3.30.00/hic_tools.3.30.00.jar',
        section_title=None,
        description='The HiCTools path',
    ),
    'multiqc_methods_description': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Generic options',
        description='Custom MultiQC yaml file containing HTML including a methods description.',
    ),
    'skip_cutadapt': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title='Pipeline controler',
        description="skip trim 5'end",
    ),
    'resample_pairs': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='resample the pairs by pairtools',
    ),
    'skip_fastqc': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='skip fastqc or not',
    ),
    'skip_peak_annotation': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='skip peak annotation or not',
    ),
    'skip_diff_analysis': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='skip differential analysis or not',
    ),
    'skip_multiqc': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='skip multiqc or not',
    ),
    'do_apa': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='run APA or not',
    ),
    'skip_compartments': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='skip call compartment or not',
    ),
    'skip_tads': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='skip call TADs or not',
    ),
    'skip_interactions': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='skip call interactions/loops',
    ),
    'do_tfea': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Do Transcription Factor Enrichment Analysis or not',
    ),
    'create_virtual_4c': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='create track files for virtual 4c or not',
    ),
    'skip_circos': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='skip circos plot',
    ),
}

