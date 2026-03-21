from setuptools import setup
setup(
    name="agent-wallet",
    version="0.1.0",
    py_modules=["agent_wallet"],
    install_requires=["cryptography>=41.0"],
    python_requires=">=3.9",
)
