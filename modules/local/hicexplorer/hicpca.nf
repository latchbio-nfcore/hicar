process HICEXPLORER_HICPCA {
    tag "${meta.id}"
    label 'process_medium'

    conda (params.enable_conda ? "bioconda::hicexplorer=3.7.2" : null)
    container "${ workflow.containerEngine == 'singularity' && !task.ext.singularity_pull_docker_container ?
        'https://depot.galaxyproject.org/singularity/hicexplorer:3.7.2--pyhdfd78af_1' :
        'quay.io/biocontainers/hicexplorer:3.7.2--pyhdfd78af_1' }"

    input:
    tuple val(meta), path(cool)

    output:
    tuple val(meta), path("${prefix}_*")              , emit:pca
    tuple val(meta), path("${prefix}_pca1.$format")   , emit:pca1
    tuple val(meta), path("${prefix}_pca2.$format")   , emit:pca2
    path("versions.yml")                              , emit:versions

    script:
    def args = task.ext.args ?: ''
    prefix = task.ext.prefix ?: "${meta.id}_${meta.bin}"
    args = args.tokenize()
    def idx = args.findIndexOf{ it == '--format' | it == '-f' }
    format = 'bigwig'
    if (idx>=0) {
        format = args[idx+1]
        args.remove(idx+1)
        args.remove(idx)
    }
    idx = args.indexOf('--whichEigenvectors')
    eigenvectors = '1 2'
    if(idx>=0) {
        eigenvectors = args[idx + 1]
        args.remove(idx+1)
        args.remove(idx)
    }
    outfilenames = eigenvectors.tokenize()
        .collect{"${prefix}_pca${it}.${format}"}.join(' ')
    args = args.join(' ')
    """
    hicPCA \\
        -m $cool \\
        $args \\
        --format $format \\
        --whichEigenvectors $eigenvectors \\
        --outputFileName $outfilenames

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        hicexplorer: \$(hicPCA --version 2>&1 | sed 's/hicPCA //')
    END_VERSIONS
    """
}
