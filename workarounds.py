# Real name for a package on pypi
# For some reason, the list of used packages has some of these names wrong
PACKAGES_REAL_NAME = {
    'backports-csv': 'backports.csv',
    'backports-functools-lru-cache': 'backports.functools-lru-cache',
    'backports-tempfile': 'backports.tempfile',
    'backports-weakref': 'backports.weakref',
    'backports-zoneinfo': 'backports.zoneinfo',
    'jaraco-classes': 'jaraco.classes',
    'jaraco-collections': 'jaraco.collections',
    'jaraco-context': 'jaraco.context',
    'jaraco-functools': 'jaraco.functools',
    'jaraco-text': 'jaraco.text',
    'jax': 'jax[cpu]',
    'pdfminer-six': 'pdfminer.six',
    'randomstuff-py': 'randomstuff.py',
    'ruamel-yaml': 'ruamel.yaml',
    'ruamel-yaml-clib': 'ruamel.yaml.clib',
    'zc-lockfile': 'zc.lockfile',
    'zope-deprecation': 'zope.deprecation',
    'zope-event': 'zope.event',
    'zope-interface': 'zope.interface',
}

# What is the name to import for a given package
# Used when even heuristics fail
PACKAGE_IMPORT_NAME = {
    'argon2-cffi-bindings': '_argon2_cffi_bindings',
    'beautifulsoup4': 'bs4',
    'databricks-sql-connector': 'databricks.sql',
    'dnspython': 'dns',
    'jpype1': 'jpype',
    'markdown-it-py': 'markdown_it',
    'oldest-supported-numpy': 'numpy',
    'opentelemetry-api': 'opentelemetry',
    'opentelemetry-exporter-otlp': 'opentelemetry.exporter.otlp.proto.grpc',
    'opentelemetry-exporter-otlp-proto-grpc': 'opentelemetry.exporter.otlp.proto.grpc',
    'opentelemetry-exporter-otlp-proto-http': 'opentelemetry.exporter.otlp.proto.http',
    'opentelemetry-instrumentation': 'opentelemetry.instrumentation',
    'opentelemetry-proto': 'opentelemetry.proto',  # No actual code, just configs
    'opentelemetry-semantic-conventions': 'opentelemetry.semconv',  # No actual code, just configs
    'opentelemetry-sdk': 'opentelemetry.sdk',
    'pymupdf': 'fitz',
    'poetry-core': 'poetry.core',
    'protobuf': 'google.protobuf',
    'pypdf2': 'PyPDF2',
    'pystan': 'stan',
    'python-multipart': 'multipart',
    'ruamel.yaml.clib': '_ruamel_yaml',
    'scikit-image': 'skimage',
}

# Packages which are needed, but are missing, for some reason
CUSTOM_PACKAGE_REQUIREMENTS = {
    'opensearch-py': ['requests'],
    'jupyterlab-pygments': ['pygments'],
    'keras': ['tensorflow'],
    'pydeequ': ['pyspark'],  # TODO: Spark version
    'graphframes': ['pyspark'],
    'jupyter-server-terminals': ['jupyter-server'],
    'nvidia-cudnn-cu11': ['nvidia-pyindex'],
    'matplotlib-inline': ['matplotlib', 'ipython'],
    'ml-dtypes': ['wheelhouse'],
    'mypy-boto3-appflow': ['botocore'],
    'mypy-boto3-rds': ['botocore'],
    'mypy-boto3-redshift-data': ['botocore'],
    'mypy-boto3-s3': ['boto3'],
    'ruamel.yaml.clib': ['ruamel.yaml'],
    'soupsieve': ['beautifulsoup4'],
    'spark-nlp': ['pyspark', 'numpy'],
    'telethon-session-sqlalchemy': ['telethon'],
    'tensorflow-addons': ['tensorflow'],
    'tensorflow-estimator': ['six', 'tensorflow'],
    'tensorflow-hub': ['tensorflow'],
    'tensorflow-io-gcs-filesystem': ['tensorflow'],
    'tf-estimator-nightly': ['six', 'tensorflow'],
}
