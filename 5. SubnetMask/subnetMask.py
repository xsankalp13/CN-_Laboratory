def calculate_subnet_mask(prefix_length):
    subnet_mask = (1 << 32 - prefix_length) - 1
    subnet_mask_str = ".".join(str((subnet_mask >> i) & 0xFF) for i in [24, 16, 8, 0])
    return subnet_mask_str


def demonstrate_subnetting(base_ip_address, prefix_length):
    subnet_mask = calculate_subnet_mask(prefix_length)
    print("Base IP Address: " + base_ip_address)
    print("Prefix Length: /" + str(prefix_length))
    print("Subnet Mask: " + subnet_mask)


# Example usage
if __name__ == "__main__":
    base_ip_address = "192.168.1.0"
    network_prefix_length = 16
    # For example, use a /24 network

    demonstrate_subnetting(base_ip_address, network_prefix_length)