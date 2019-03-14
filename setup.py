from setuptools import setup
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == '__main__':
    setup(
        name = 'wisp',
        version="0.0.8-beta",
        description = 'A preference based location finder app',
        author = 'Jimut Bahan Pal',
        author_email = 'paljimutbahan@gmail.com',
        maintainer = 'Jimut Bahan Pal',
        maintainer_email = 'paljimutbahan@gmail.com',
        url = '',
        license = 'GPLv2+',
        platforms = 'Linux',
        py_modules = ['wisp'],
        entry_points = {
            'console_scripts': ['wisp = wisp:main'],
        },
        include_package_data = True,
        install_requires = [
            'requests',
            'datetime',
            'IPython',
            'pandas',
            'folium',
            'geopy',     
            'numpy',
            'wget',
            'pip'
        ],
        keywords = 'Preference, location, wisp, requests, html, json, numpy, pandas, software, tkinter, folium, geopy, lat lon, wget, Ipython, location cluster, KNN, Machine learning, clustering',
        classifiers = [
                'Development Status :: 0.0.8 - Beta',
                'Environment :: Console',
                'Intended Audience :: End Users/Desktop',
                'Intended Audience :: System Administrators',
                'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
                'Operating System :: Manjaro',
                'Programming Language :: Python :: 3.7.2',
                'Topic :: Internet :: WWW/HTTP',
                'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
                ],
)
