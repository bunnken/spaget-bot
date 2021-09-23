from discord.ext import commands

class System(commands.Cog):

    @commands.Cog.listener()
    async def on_ready(self):
        print("Spaget is ready")


def setup(bot):
    bot.add_cog(System(bot))
