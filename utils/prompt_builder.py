def generate_outfit_prompt(aesthetic, recommendations):

    tops = ", ".join(recommendations["tops"])
    bottoms = ", ".join(recommendations["bottoms"])
    shoes = ", ".join(recommendations["shoes"])

    prompt = f"""
    High quality fashion outfit,
    {aesthetic} aesthetic,
    featuring {tops},
    paired with {bottoms},
    and {shoes},
    realistic fashion photography,
    modern instagram fashion style,
    clean background,
    highly detailed
    """

    return prompt