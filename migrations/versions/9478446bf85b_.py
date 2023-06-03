"""empty message

Revision ID: 9478446bf85b
Revises:
Create Date: 2023-05-31 19:59:47.649289

"""
from alembic import op
import sqlalchemy as sa
import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = '9478446bf85b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    if environment == "production":
        op.execute(f"ALTER TABLE songs SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###qqqqqqqqq
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    # sa.Column('first_name', sa.String(length=255), nullable=False),
    # sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('cover_photo_url', sa.String(length=255), nullable=True),
    # sa.Column('theme', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('playlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('cover_photo_url', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # # ### end Alembic commands ###
    if environment == "production":
        op.execute(f"ALTER TABLE albums SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###qqqqqqqqq
# ...
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=False),
    sa.Column('artist', sa.String(length=255), nullable=False),
    sa.Column('album', sa.String(length=255), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),  # Updated data type
    sa.Column('cover_photo_url', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
)
# ...


    # # ### end Alembic commands ###
    if environment == "production":
        op.execute(f"ALTER TABLE albums SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###qqqqqqqqq
    op.create_table('playlist_songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('playlist_id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlists.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('playlist_songs')
    op.drop_table('songs')
    op.drop_table('playlists')
    op.drop_table('users')