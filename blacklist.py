# DISABLE_MSVC = False
DISABLE_MSVC = True
USE_SERVERCORE_IMAGE = True

BLACKLIST = {
    'both': {
        'azure',  # Marked as deprecated
        'azure-keyvault',  # Metapackage, just installs other packages in the top1000
        'azure-mgmt',  # Deprecated
        'azure-mgmt-datalake-nspkg',  # Empty namespace package
        'azure-mgmt-nspkg',  # Empty namespace package
        'azure-nspkg',  # Empty namespace package
        'azure-storage',  # Deprecated, do not use
        'azureml-dataprep-rslex',  # Not intended for direct installation
        'botocore-stubs',  # Just mypy stubs, no code, nothing to test
        'bs4',  # Dummy package, use beautifulsoup4
        'futures',  # Python 3 not supported
        'google-cloud',  # Deprecated empty package
        'sklearn',  # "Use scikit-learn instead"
        'types-s3transfer',  # Just mypy stubs, no code, nothing to test
        'types-awscrt',  # Just mypy stubs, no code, nothing to test
        'tensorflow-io-gcs-filesystem',  # I THINK that this is not supposed to be used directly

        # Bug in library / requirement unsatisfied
        'flask-oidc',  # https://github.com/puiterwijk/flask-oidc/pull/141
        'spark-sklearn',  # Old lib with old dependencies on scikit-learn
        'imbalanced-learn',  # imports _joblib_parallel_args from the wrong place

        # "lolnope" doesn't work
        'sekkaybot',  # Some kind of personal bot or sth... (+uvloop on windows)
        'tfx-bsl',  # Wheels only 3.6-3.8 (win/lin)
    },
    'windows': {
        # Not supported on Windows
        'ansible',  # Doesn't support windows
        'ansible-core',  # Doesn't support windows
        'blessings',  # Requires curses
        'dockerpty',  # Requires fnctl
        'nvidia-cudnn-cu11',  # Doesn't seem to have wheels for windows
        'nvidia-nccl-cu11',  # Doesn't seem to have wheels for windows
        'ptyprocess',  # Requires fnctl
        'pystan',  # https://pystan2.readthedocs.io/en/latest/windows.html
        'fbprophet',  # requires pystan
        'python-daemon',  # Requires pwd module (also daemons are only on unix)
        'sasl',  # Cyrus SASL on Windows is still laregely a "work in progress"
        'sekkaybot',  # Requires uvloop
        'sh',  # Requires fnctl
        'triton',  # Not supported on Windows
        'uvloop',  # Not supported on Windows
        'uwsgi',  # Not supported on Windows

        # Requires DLL or external setup
        'fiona',
        'geopandas',  # Requires fiona
        # 'gitpython',
        # 'opencv-python',
        'pycurl',  # libcurl
        'pygobject',  # Msvc not supported https://gitlab.gnome.org/GNOME/pygobject/-/issues/454
        # 'xgboost',  # xgboost.dll

        # Bug in library / requirement unsatisfied
        'python-magic',  # wrong dependency on python 3.8+ https://github.com/dveselov/python-libmagic/issues/8#issuecomment-1040880668
        'pycrypto',  # "PyCrypto is dead" https://github.com/pycrypto/pycrypto/issues/238

        # Requires C++ compiler
        'tensorflow-transform',  # Old pyarrow dependency which installs numpy

        # "lolnope" doesn't work
        'tfx-bsl',  # Wheels only 3.6-3.8 (win/lin)
    },
    'linux': {
        # Not supported on Linux
        'pywin32',

        # Requires DLL or external setup
        # 'fiona',
        # 'gitpython',
        # 'lightgbm',  # libgomp.so.1
        # 'mysqlclient',  # mysql_config not found
        # 'opencv-python',  # libGL.so.1
        # 'pattern',  # Requires mysqlclient
        # 'psycopg2',  # pg_config
        # 'pycairo',  # pkg-config
        # 'pycurl',  # curl-config
        # 'pygobject',  # Requires pycairo
        # 'python-magic',  # libmagic

        # Requires C++ compiler
        # 'ciso8601',
        # 'pycrypto',
        # 'pyminizip',
        # 'pyodbc',
        # 'python-levenshtein',
        # 'sasl',
        'tensorflow-transform',  # Old pyarrow dependency which installs numpy
        # 'uwsgi',

        'nvidia-cudnn-cu11',  # Only C lib files. Hard to check

        # Fails to compile
        'backports.zoneinfo',  # Wontfix
    }
}

if DISABLE_MSVC:
    BLACKLIST['windows'] = BLACKLIST['windows'].union({
        'backports.zoneinfo',
        'ciso8601',
        'dbt-snowflake',
        'netifaces',
        'pyminizip',
        'python-levenshtein',
        'python-keystoneclient',  # Requires netifaces
        'sasl',  #!
        'snowflake-connector-python',
        'snowflake-sqlalchemy',  # Requires snowflake-connector-python
    })

if USE_SERVERCORE_IMAGE:
    BLACKLIST['windows'] = BLACKLIST['windows'].union({
        'opencv-python',
    })
