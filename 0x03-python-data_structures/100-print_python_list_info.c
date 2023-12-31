#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p) 
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = Py_SIZE(list);
    Py_ssize_t allocated = list->allocated;
    
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);
    
    for (Py_ssize_t x = 0; x < size; x++) 
    {
        PyObject *item = PyList_GetItem(p, x);
        const char *item_type = Py_TYPE(item)->tp_name;
        printf("Element %ld: %s\n", x, item_type);
    }
}
