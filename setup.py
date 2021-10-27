from setuptools import setup


setup(
    name='cldfbench_dunn_et_al2011',
    py_modules=['cldfbench_dunn_et_al2011'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'dunn_et_al2011=cldfbench_dunn_et_al2011:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
