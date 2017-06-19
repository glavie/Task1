def update(config, service_name, count):
    """Update config with new instances."""
    new_config = {key: dict(value) for key, value in config.items()}
    for _ in range(count):
        m_key, m_val = min(
            new_config.items(),
            key=lambda item: (sum(item[1].values()), item[0]),
        )
        m_val.setdefault(service_name, 0)
        m_val[service_name] += 1
    return new_config


def test_initial():
    config = {
        'ginger': {},
        'cucumber': {},
    }

    config = update(config, 'flask', 3)
    config = update(config, 'django', 3)

    assert sum(config['ginger'].values()) == sum(config['cucumber'].values())
    assert sum(sum(x.values()) for x in config.values()) == 3+3


if __name__ == '__main__':
    test_initial()
