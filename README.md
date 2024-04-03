# Polygon Inclusion Algorithms

This repository contains implementations of various algorithms for determining whether a point is inside a polygon, and for finding inclusions of polygons within each other. The algorithms implemented are:

1. Ray Tracing Method
2. Winding Number Method
3. Cross Product Method
4. Peucker and Doo Algorithm (for polygon simplification)

You can find my journey of building it in the rapport.txt

## Usage

To use the algorithms, first install the required dependencies by running:
```
pip install numpy matplotlib
```
Then, you can use the `main.py` script to read in polygons from .poly files, find inclusions, and print the results in a text format. For example:
```
python main.py 10x10.poly e2.poly
```
To benchmark the speed of each method on a given set of polygons, edit the `main.py` script :
```
if __name__ == "__main__":
    main()
    #run_benchmark()
```
to 
```
if __name__ == "__main__":
    #main()
    run_benchmark()
```
```
python main.py 10x10.poly e2.poly
```
To generate test files with random polygons, use the `generate_test_files.py` script. For example:
```
python generate_test_files.py
```
It will generate various .poly files to test simple scenes and a randomly_generated.poly file that is composed of randomly generated polygons based on the following parameters : 
```
You can edit parameters here :
n = 4000
m = 50
min_coord = -100000000
max_coord = 100000000
```
This will generate 4000 random polygons with 50 angles in each.

## Performance

The performance of each algorithm was tested on a set of polygons with varying numbers of vertices and complexity without the Peucker optimisation. The results are shown below:

| Number of Polygons | Number of Vertices | Ray Tracing Method (seconds) | Winding Number Method (seconds) | Cross Product Method (seconds) |
| --- | --- | --- | --- | --- |
| 400 | 50 | 0.24 | 0.13 | 0.11 |
| 4000 | 50 | 2.36 | 1.30 | 1.13 |
| 400 | 300 | 8.20 | 4.59 | 4.02 |

The Cross Product Method consistently outperformed the other methods, especially for polygons with a large number of vertices.

## Optimization

The Peucker and Doo Algorithm was used to simplify the polygons and improve the performance of the other algorithms. The results with a threshold of 90000000 are shown below:

| Number of Polygons | Number of Vertices | Ray Tracing Method (seconds) | Winding Number Method (seconds) | Cross Product Method (seconds) |
| --- | --- | --- | --- | --- |
| 400 | 50 | 0.05 | 0.03 | 0.02 |
| 4000 | 50 | 0.47 | 0.26 | 0.21 |
| 400 | 300 | 1.49 | 0.83 | 0.69 |

The optimization significantly improved the performance of all algorithms, especially for polygons with a large number of vertices.

## Conclusion

The Cross Product Method was found to be the fastest algorithm for determining whether a point is inside a polygon, and the Peucker and Doo Algorithm was found to be effective at simplifying polygons and improving the performance of all algorithms.

## License

This project is licensed under the MIT License.

## Acknowledgements

The implementation of the Winding Number Method was based on the algorithm described in [this article](https://en.wikipedia.org/wiki/Point_in_polygon).

The implementation of the Peucker and Doo Algorithm was based on the algorithm described in [this article](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm).

The implementation of the Cross Product Method was based on the algorithm described in [this article](https://en.wikipedia.org/wiki/Cross_product).

The implementation of the Ray Tracing Method was based on the algorithm described in [this article](https://fr.wikipedia.org/wiki/Algorithme_de_d%C3%A9tection_de_collision_rayon-polygone).

The implementation of the benchmarking code was based on the code described in [this article](https://realpython.com/python-benchmark-tools/).

The implementation of the polygon generation code was based on the code described in [this article](https://stackoverflow.com/questions/36276889/generate-random-polygons-in-python).

The implementation of the polygon visualization code was based on the code described in [this article](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html).

The implementation of the command line argument parsing code was based on the code described in [this article](https://docs.python.org/3/library/argparse.html).