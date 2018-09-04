#distutils: language = c++

cdef extern from "sum.hpp":
    cdef cppclass Sum:
        Sum() except +
        int get_current_sum()
        void add(int)
