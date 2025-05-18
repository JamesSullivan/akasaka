# %% Cell 1
import datetime
import os
from typing import Dict, List, Any

from sqlalchemy import create_engine, text, select, and_
from sqlalchemy.orm import Session, aliased

from models import Sub, Pre, Num


class Query:
    def __init__(self):
        password: str = os.environ.get("AKASAKA_DB_PW", "default_password")
        # Set up the connection to PostgreSQL
        self.engine = create_engine(
            f"postgresql://puser:{password}@localhost:5432/fin_report"
        )
        self.companies: List[str] = []
        self.company_cik: Dict[str, int] = {}
        with self.engine.connect() as connection:
            result = connection.execute(text("select distinct(name), cik from sub;"))
            for row in result:
                self.companies.append(row.name)
                self.company_cik[row.name] = row.cik

    def cik_adsh(self, cik: int) -> List[Dict[str, Any]]:
        """
        Get the adshs and datetimes from the database.
        """
        list_of_dicts: List[Dict] = []
        with self.engine.connect() as connection:
            # result: CursorResult = connection.execute(text("select distinct(cik), adsh from sub where cik = :cik"), {'cik': cik})
            result = connection.execute(
                text(
                    "select distinct(adsh), filed, fy, fp from sub where cik= :cik and form='10-K' order by fy, fp;"
                ),
                {"cik": cik},
            )
            list_of_dicts = [
                {"adsh": r.adsh, "filed": r.filed, "fy": r.fy, "fp": r.fp}
                for r in result
            ]
        return list_of_dicts

    def adsh_stmt(self, adsh: str, stmt: str) -> List[Dict[str, Any]]:
        # Select from the Pre table with the specified filters
        print(f"adsh: {adsh}, stmt: {stmt}")
        statement_query = (
            select(Pre)
            .where(and_(Pre.stmt == stmt, Pre.adsh == adsh))
            .subquery()
            .alias("statement")
        )  # Using subquery().alias() to represent the 'statement' result set for joining

        # Perform the left join with the Num table
        # We need to use the aliased 'statement' for the join conditions
        query = (
            select(statement_query, Num)
            .select_from(statement_query)
            .join(
                Num,
                and_(
                    statement_query.c.adsh == Num.adsh,
                    statement_query.c.tag == Num.tag,
                    statement_query.c.version == Num.version,
                    Num.dimh == "0x00000000",
                    Num.iprx == 0,
                ),
                isouter=True,  # This makes it a LEFT JOIN
            )
        )

        # Add the order by clause
        query = query.order_by(statement_query.c.line)

        # To execute the query and get results:
        with Session(self.engine) as session:
            results = session.execute(query).mappings().all()
            list_of_dicts: List[Dict] = []
            for r in results:
                pre = dict(r)
                num = pre["Num"]
                pre.pop("Num")
                if num is None:
                    list_of_dicts.append(pre)
                else:
                    num_dict = r["Num"].as_dict()
                    list_of_dicts.append({**pre, **num_dict})
            return list_of_dicts
        return []


query = Query()
target_cik = query.company_cik["MICROSOFT CORP"]
print(f"{target_cik}")
# results = query.cik_adsh(target_cik)
# results = query.adsh_stmt("0000950170-23-014423", "IS")
results = query.adsh_stmt("0001193125-16-662209", "IS")
print(results)

# %%
