config = {
    "server": {
        "host": "127.0.0.1",
        "port": 8080,
        "ssl": {
            "enabled": True,
            "cert_path": "/etc/ssl/certs"
            }
        },
    "database": "postgresql://localhost:5432"
    }


def traverse_nested_config(config_dict, path_str, default=None):
    if not path_str:
        return default
    
    paths = path_str.split('.')
    try:
        value = config_dict
        for path in paths:
            value = value[path]
            
        return value
    except (KeyError, TypeError, AttributeError):
        return default
    
print(traverse_nested_config(config, "server.ssl.cert_path"))