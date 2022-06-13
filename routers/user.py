from fastapi import APIRouter, Body, Depends, HTTPException
from dto.user import User

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

router = APIRouter(
    prefix="/users",
    tags=["User CRUD"],
    # dependencies=[Depends(get_current_active_user)],
     responses={404: {"description": "Not found"}},
)

@router.get("/{item_id}", response_model=User)
async def get_item_by_id(item_id: int):
    item = [item for item in fake_items_db if item["item_id"] == item_id]
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/", response_model=User)
async def get_items(skip: int = 0, limit: int = 10):
    return {"items": fake_items_db[skip:limit+skip]}
