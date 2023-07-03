"""empty message

Revision ID: e1ee77b5c0de
Revises: 
Create Date: 2022-11-17 10:32:23.255619

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e1ee77b5c0de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ability',
    sa.Column('ability_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('generation', sa.String(length=300), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('ability_id'),
    sa.UniqueConstraint('ability_id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('item',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('img', sa.String(length=300), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('item_id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('item_id')
    )
    op.create_table('moves',
    sa.Column('move_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('generation', sa.String(length=300), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('accuracy', sa.Integer(), nullable=True),
    sa.Column('pp', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=120), nullable=False),
    sa.Column('damage_class', sa.String(length=120), nullable=True),
    sa.Column('power', sa.Integer(), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('move_id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('move_id')
    )
    op.create_table('nature',
    sa.Column('nature_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('decrease_stat', sa.String(length=120), nullable=True),
    sa.Column('increase_stat', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('nature_id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('nature_id')
    )
    op.create_table('pokemon',
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('img', sa.String(length=201), nullable=False),
    sa.Column('shiny', sa.String(length=122), nullable=True),
    sa.Column('type', postgresql.ARRAY(sa.String(length=300)), nullable=True),
    sa.Column('group_name', postgresql.ARRAY(sa.String(length=300)), nullable=True),
    sa.Column('weakness', postgresql.ARRAY(sa.String(length=300)), nullable=True),
    sa.Column('evolution', postgresql.ARRAY(sa.String(length=300)), nullable=True),
    sa.Column('url', sa.String(length=123), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('ps', sa.Integer(), nullable=False),
    sa.Column('spd', sa.Integer(), nullable=False),
    sa.Column('sp_defens', sa.Integer(), nullable=False),
    sa.Column('sp_atk', sa.Integer(), nullable=False),
    sa.Column('defens', sa.Integer(), nullable=False),
    sa.Column('atk', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('pokemon_id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('pokemon_id'),
    sa.UniqueConstraint('url')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('img', sa.String(length=300), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('pokemon__ability',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('ability_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ability_id'], ['ability.ability_id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.pokemon_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('pokemon__move',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('move_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['move_id'], ['moves.move_id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.pokemon_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('pokemon_fusion',
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('group_name', postgresql.ARRAY(sa.String(length=300)), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('img', sa.String(length=201), nullable=False),
    sa.Column('type', postgresql.ARRAY(sa.String(length=300)), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('ps', sa.Integer(), nullable=False),
    sa.Column('spd', sa.Integer(), nullable=False),
    sa.Column('sp_defens', sa.Integer(), nullable=False),
    sa.Column('sp_atk', sa.Integer(), nullable=False),
    sa.Column('defens', sa.Integer(), nullable=False),
    sa.Column('atk', sa.Integer(), nullable=False),
    sa.Column('votes', sa.Integer(), nullable=False),
    sa.Column('father', sa.Integer(), nullable=False),
    sa.Column('mom', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['father'], ['pokemon.pokemon_id'], ),
    sa.ForeignKeyConstraint(['mom'], ['pokemon.pokemon_id'], ),
    sa.PrimaryKeyConstraint('pokemon_id'),
    sa.UniqueConstraint('pokemon_id')
    )
    op.create_table('equipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_fusion_id', sa.Integer(), nullable=True),
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('linea', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pokemon_fusion_id'], ['pokemon_fusion.pokemon_id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.pokemon_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon_fusion.pokemon_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('pokemon__fusion__ability',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('ability_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ability_id'], ['ability.ability_id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon_fusion.pokemon_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('pokemon__fusion__move',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('move_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['move_id'], ['moves.move_id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon_fusion.pokemon_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('pokemon__fusion__nature',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('nature_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['nature_id'], ['nature.nature_id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon_fusion.pokemon_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon_fusion.pokemon_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    op.drop_table('pokemon__fusion__nature')
    op.drop_table('pokemon__fusion__move')
    op.drop_table('pokemon__fusion__ability')
    op.drop_table('favorites')
    op.drop_table('equipo')
    op.drop_table('pokemon_fusion')
    op.drop_table('pokemon__move')
    op.drop_table('pokemon__ability')
    op.drop_table('user')
    op.drop_table('pokemon')
    op.drop_table('nature')
    op.drop_table('moves')
    op.drop_table('item')
    op.drop_table('ability')
    # ### end Alembic commands ###
