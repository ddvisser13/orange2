import Orange
data = Orange.data.Table("lenses")
domain = data.domain
inst = Orange.data.Instance(domain, ["young", "myope",
                               "yes", "reduced", "soft"])
print inst
inst = Orange.data.Instance(domain, ["young", 0, 1,
            Orange.data.Value(domain[3], "reduced"), "soft"])
print inst
