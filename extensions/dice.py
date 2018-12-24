import discord
import random
import re
from discord.ext import commands as kobold


class Roll:

    def __init__(self, bot):
        self.kobold = bot

    def _build_output(self, title, r, ctx):
        # builds the embedded element that will compose the message
        embed = discord.Embed(color=discord.Color.dark_red())
        embed.title = title
        embed.description = str(r.num_rolls) + "d" + str(r.faces)
        embed.add_field(name="Roll(s)", value="+".join(str(x) for x in r.rolls))
        embed.add_field(name="Bonus", value=r.bonus)
        embed.add_field(name="Total", value=r.total)
        if r.faces == 20:
            embed.add_field(name="Crit Success", value=str(r.success))
            embed.add_field(name="Crit Fails", value=str(r.fail))
        embed.timestamp = ctx.message.timestamp
        return embed

    @kobold.command(pass_context=True)
    async def roll(self, ctx, dice: str = "1d4", bonus: str = "0"):
        """rolls a dice type the user inputs in a 1d4 format
           and adds/subtracts bonuses from the roll.Prints out into
           the text channel the command was invoked. Default die is
           1d4 and bonus default is 0."""
        d = Dice(dice, bonus)
        d.roll_dice()
        msg = self._build_output("Roll", d, ctx)
        await self.kobold.say(embed=msg)

    @kobold.command(pass_context=True)
    async def proll(self, ctx, dice: str = "1d4", bonus: str = "0"):
        """rolls a dice type the user inputs in a 1d4 format
           and adds/subtracts bonuses from the roll and send the result
           directly to the user. Perfect for behind the screen rolls.
           Default die is 1d4 and bonus default is 0."""
        d = Dice(dice, bonus)
        d.roll_dice()
        msg = self._build_output("Private roll", d, ctx)
        user = ctx.message.author
        await self.kobold.send_message(user, embed=msg)


class Dice:
    def __init__(self, dice, bonus):
        values = re.findall('[0-9][0-9]*', dice)
        self.bonus = bonus
        self.num_rolls = int(values[0])
        self.faces = int(values[1])
        self.rolls = []
        self.total = 0
        self.fail = 0
        self.success = 0

    def roll_dice(self):
        self.rolls = [random.randint(1, self.faces) for x in range(self.num_rolls)]
        if self.faces == 20:
            self.fail = self.rolls.count(1)
            self.success = self.rolls.count(20)
        self.total = sum(self.rolls)


def setup(kobold):
    kobold.add_cog(Roll(kobold))
