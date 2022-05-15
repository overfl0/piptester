BLACKLIST = {
    'windows': {
        'azure',  # Marked as deprecated
        'azure-keyvault',  # Metapackage, just installs other packages in the top1000
        'azure-mgmt',  # Deprecated
        'azure-mgmt-datalake-nspkg',  # Empty namespace package
        'azure-mgmt-nspkg',  # Empty namespace package
        'azure-nspkg',  # Empty namespace package
        'azureml-dataprep-rslex',  # Not intended for direct installation
        'bs4',  # Dummy package, use beautifulsoup4
        'google-cloud',  # Deprecated empty package
        'sklearn',  # "Use scikit-learn instead"
        'tensorflow-io-gcs-filesystem.txt',  # I THINK that this is not supposed to be used directly

        # Not supported on Windows
        'ansible',  # Doesn't support windows
        'ansible-core',  # Doesn't support windows
        'blessings',  # Requires curses
        'dockerpty',  # Requires fnctl
        'ptyprocess',  # Requires fnctl
        'pystan',  # https://pystan2.readthedocs.io/en/latest/windows.html
        'python-daemon',  # Requires pwd module (also daemons are only on unix)
        'sekkaybot',  # Requires uvloop
        'sh',  # Requires fnctl
        'uvloop',  # Not supported on Windows
        'uwsgi',  # Not supported on Windows

        # Requires DLL or external setup
        # 'fiona',
        # 'geopandas',
        # 'gitpython',
        # 'graphframes',  # SPARK_HOME
        # 'opencv-python',
        # 'pycurl',  # libcurl
        # 'python-magic',  # libmagic
        # 'xgboost',  # xgboost.dll

        # Bug in library / requirement unsatisfied
        'flask-oidc',  # https://github.com/puiterwijk/flask-oidc/pull/141
        'spark-sklearn',  # Old lib with old dependencies on scikit-learn
        'imbalanced-learn',  # imports _joblib_parallel_args from the wrong place

        # Requires C++ compiler
        # 'backports.zoneinfo',
        # 'ciso8601',
        # 'dbt-snowflake',
        # 'netifaces',
        # 'pycrypto',
        # 'pygobject',
        # 'pyminizip',
        # 'python-levenshtein',
        # 'python-keystoneclient',  # Requires netifaces
        # 'sasl',
        # 'snowflake-connector-python',
        # 'snowflake-sqlalchemy',  # Requires snowflake-connector-python
        'tensorflow-transform',  # Old pyarrow dependency which installs numpy

        # "lolnope" doesn't work
        'constructs',
        'tfx-bsl',  # Wheels only 3.6-3.8 (win/lin)
    },
    'linux': {
        'azure',  # Marked as deprecated
        'azure-keyvault',  # Metapackage, just installs other packages in the top1000
        'azure-mgmt',  # Deprecated
        'azure-mgmt-datalake-nspkg',  # Empty namespace package
        'azure-mgmt-nspkg',  # Empty namespace package
        'azure-nspkg',  # Empty namespace package
        'azureml-dataprep-rslex',  # Not intended for direct installation
        'bs4',  # Dummy package, use beautifulsoup4
        'google-cloud',  # Deprecated empty package
        'sklearn',  # "Use scikit-learn instead"
        'tensorflow-io-gcs-filesystem.txt',  # I THINK that this is not supposed to be used directly

        # Not supported on Linux
        'pywin32',

        # Requires DLL or external setup
        #'fiona',
        #'gitpython',
        #'graphframes',  # SPARK_HOME
        #'lightgbm',  # libgomp.so.1
        #'mysqlclient',  # mysql_config not found
        #'opencv-python',  # libGL.so.1
        #'pattern',  # Requires mysqlclient
        #'psycopg2',  # pg_config
        #'pycairo',  # pkg-config
        #'pycurl',  # curl-config
        #'pygobject',  # Requires pycairo
        #'python-magic',  # libmagic

        # Bug in library / requirement unsatisfied
        'flask-oidc',  # https://github.com/puiterwijk/flask-oidc/pull/141
        'spark-sklearn',  # Old lib with old dependencies on scikit-learn
        'imbalanced-learn',  # imports _joblib_parallel_args from the wrong place

        # Requires C++ compiler
        #'backports.zoneinfo',
        #'ciso8601',
        #'pycrypto',
        #'pyminizip',
        #'pyodbc',
        #'python-levenshtein',
        #'sasl',
        'tensorflow-transform',  # Old pyarrow dependency which installs numpy
        #'uwsgi',

        # "lolnope" doesn't work
        'constructs',
        'sekkaybot',  # Some kind of personal bot or sth...
        'tfx-bsl',  # Wheels only 3.6-3.8 (win/lin)
    }
}
