from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='cldfbench_hochstetler2004sociolinguistic',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['cldfbench_hochstetler2004sociolinguistic'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'hochstetler2004sociolinguistic=cldfbench_hochstetler2004sociolinguistic:Dataset',
        ]
    },
    install_requires=[
        'pyglottography>=2.0',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
