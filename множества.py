# class A:
#     def method(self):
#         print('Its method in class A')
#
#
# class B:
#
#     def method_b(self):
#         print('Its method in class B')
#
#
# class C(A, B):
#     pass
#
#
# exem_c = C()
# exem_c.method()
# exem_c.method_b()
#
# print(exem_c)


class A:

    def method_a(self):
        print('its method in class A')


class B(A):
    def method_a(self):
        print('its method in class B')


class C(A):
    def method_a(self):
        print('its method in class C')


class D(B, C):
    pass


exem_d = D()
exem_d.method_a()
