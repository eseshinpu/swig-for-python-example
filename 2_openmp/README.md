## swig compile command
```
swig -c++ -python multithread.i
python setup.py build_ext --inplace
```

## Time to loop 100,000 times just to output text
```
python normal loop: 22.01766872406006 sec
cpp normal loop: 0.025933265686035156 sec
cpp openmp loop: 0.03390789031982422 sec
```