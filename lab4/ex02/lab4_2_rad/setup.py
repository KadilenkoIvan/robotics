from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'lab4_2_rad'

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
             glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
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
            'static_broadcaster = lab4_2_rad.static_broadcaster:main',
            'carrot_broadcaster = lab4_2_rad.carrot_broadcaster:main',
            'turtle_follower = lab4_2_rad.turtle_follower:main',
            'turtle_spawner = lab4_2_rad.turtle_spawner:main',
        ],
    },
)
