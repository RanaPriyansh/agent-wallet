from setuptools import setup
setup(
    name="thielon-agent-wallet",
    version="0.1.0",
    py_modules=["thielon_wallet"],
    install_requires=["cryptography>=41.0"],
    python_requires=">=3.9",
)
