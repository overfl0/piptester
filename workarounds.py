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
    'dnspython': 'dns',
    'jpype1': 'jpype',
    'oldest-supported-numpy': 'numpy',
    'pymupdf': 'fitz',
    'poetry-core': 'poetry.core',
    'ruamel.yaml.clib': '_ruamel_yaml',
}

# Packages which are needed, but are missing, for some reason
CUSTOM_PACKAGE_REQUIREMENTS = {
    'opensearch-py': ['requests'],
    'jupyterlab-pygments': ['pygments'],
    'keras': ['tensorflow'],
    'pydeequ': ['pyspark'],  # TODO: Spark version
    'ruamel.yaml.clib': ['ruamel.yaml'],
    'soupsieve': ['beautifulsoup4'],
    'tensorflow-addons': ['tensorflow'],
    'tensorflow-estimator': ['six', 'tensorflow'],
    'tensorflow-hub': ['tensorflow'],
    'tensorflow-io-gcs-filesystem': ['tensorflow'],
    'tf-estimator-nightly': ['six', 'tensorflow'],
}