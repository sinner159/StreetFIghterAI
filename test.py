import retro
sfgame='StreetFighterIISpecialChampionEdition-Genesis'

def main():
    env = retro.make(game=sfgame)
    obs = env.reset()
    while True:
        a = env.action_space.sample()
        obs, rew, done, info = env.step(a)
        env.render()
        if done:
            obs = env.reset()
    env.close()


if __name__ == "__main__":
    main()