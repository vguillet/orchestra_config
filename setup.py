from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'orchestra_config'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*_launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vguillet',
    maintainer_email='victor.guillet@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'orchestra_config = orchestra_config.orchestra_config:main',
            'controller_graph = controller_graph.controller_graph:main',
            'maaf_allocation_node = maaf_allocation_node.maaf_allocation_node:main',
            'mbawi_sim = mbawi_sim.mbawi_sim:main',
            'rlb_simple_sim = rlb_simple_sim.RLB_simple_sim:main'
        ],
    },
)
