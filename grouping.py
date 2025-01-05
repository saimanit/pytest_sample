class TestClass:
    def test_one(self):
        x = 'mani'
        assert 'a' in x
        
    def test_two(self):
        x = 'hello'
        assert hasattr(x, "hello")