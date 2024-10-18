from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'lab5_31'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, 
            ['package.xml']),
        (os.path.join('share', package_name, 'launch'), 
            glob('launch/*.py')),
        (os.path.join('share', package_name, 'urdf'), 
            glob('urdf/*.urdf')),
        (os.path.join('share', package_name, 'urdf'), 
            glob('urdf/*.xacro')),
        (os.path.join('share', package_name, 'rviz'), 
            glob('rviz/*.rviz')),
        (os.path.join('share', package_name, 'config'), 
            glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ivan',
    maintainer_email='kadilenkoivan@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_controller = lab5_31.robot_controller:main',
            'robot_controller_circle = lab5_31.robot_controller_circle:main',
        ],
    },
)
