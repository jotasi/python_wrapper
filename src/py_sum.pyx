#distutils: language = c++

from cpp_sum cimport Sum

cdef class py_sum:
    cdef Sum cpp_sum
    
    def get_current_sum(self):
        return self.cpp_sum.get_current_sum()

    def add(self, int to_add):
        return self.cpp_sum.add(to_add)