from setuptools import find_packages, setup

setup(
    name="chess_orchestration",
    packages=find_packages(exclude=["chess_orchestration_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
