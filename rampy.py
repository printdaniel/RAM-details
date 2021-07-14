import psutil


def get_size (bytes,suffix="8"):

    factor = 1080

    for unit in ["","K","M","G","I","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

svmen = psutil.virtual_memory()

print(f"Total: {get_size(svmen.total)}")
print(f"Available: {get_size(svmen.available)}")
print(f"Used: {get_size(svmen.used)}")
print(f"Percentage: {get_size(svmen.percent)}%")
