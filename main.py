from pysc2.env import sc2_env
from pysc2.lib import actions, features

from zerg import ZergAgent

from absl import app

def main(unused_argv):
	agent = ZergAgent()
	map = 'AbyssalReef'
	try:
		while True:
			with sc2_env.SC2Env(
				map_name = map,
				players = [sc2_env.Agent(sc2_env.Race.zerg), sc2_env.Bot(sc2_env.Race.random, sc2_env.Difficulty.very_easy)],
				agent_interface_format=features.AgentInterfaceFormat(feature_dimensions = features.Dimensions(screen = 84, minimap = 64), use_feature_units = True),
				step_mul = 16,
				game_steps_per_episode = 0,
				visualize = False) as env:
					agent.setup(env.observation_spec(), env.action_spec())

					timesteps = env.reset()
					agent.reset()

					while True:
						step_actions = [agent.step(timesteps[0])]
						if timesteps[0].last():
							break
						timesteps = env.step(step_actions)

	except KeyboardInterrupt:
		pass

if __name__ == "__main__":
	app.run(main)