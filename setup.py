from setuptools import setup, find_packages

setup(
    name='smart_todo_agent',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A beginner-friendly AI agent that smartly schedules to-do tasks.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/smart-todo-ai-agent',
    packages=find_packages(include=['smart_todo_agent', 'smart_todo_agent.*']),
    install_requires=[
        'pandas>=1.3.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'run-agent=smart_todo_agent.run_agent:main',
        ],
    }
)
