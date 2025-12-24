s = input()
prefix = input()
suffix = input()

starts_correctly = s.startswith(prefix)
ends_correctly = s.endswith(suffix)

print(starts_correctly and ends_correctly)