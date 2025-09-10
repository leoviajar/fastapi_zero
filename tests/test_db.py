from dataclasses import asdict

from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='leonardo', password='secret', email='leo@example.com'
        )
        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'leonardo'))

    assert asdict(user) == {
        'id': 1,
        'username': 'leonardo',
        'password': 'secret',
        'email': 'leo@example.com',
        'created_at': time,
    }
