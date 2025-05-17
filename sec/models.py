import datetime
from typing import Optional
from sqlalchemy import Column, Integer, BigInteger, Float, Text, TIMESTAMP, Boolean
from sqlalchemy.orm import declarative_base

# Define a base class for declarative models
Base = declarative_base()

class Sub(Base):
    """
    SQLAlchemy ORM model for the 'sub' table (updated definition).
    """
    __tablename__ = 'sub'

    adsh: str = Column(Text, primary_key=True)
    cik: Optional[int] = Column(BigInteger)
    name: Optional[str] = Column(Text)
    sic: Optional[float] = Column(Float)
    countryba: Optional[str] = Column(Text)
    stprba: Optional[str] = Column(Text)
    cityba: Optional[str] = Column(Text)
    zipba: Optional[str] = Column(Text)
    bas1: Optional[str] = Column(Text)
    bas2: Optional[float] = Column(Float)
    baph: Optional[str] = Column(Text)
    countryma: Optional[str] = Column(Text)
    stprma: Optional[str] = Column(Text)
    cityma: Optional[str] = Column(Text)
    zipma: Optional[str] = Column(Text)
    mas1: Optional[str] = Column(Text)
    mas2: Optional[float] = Column(Float)
    countryinc: Optional[str] = Column(Text)
    stprinc: Optional[str] = Column(Text)
    ein: Optional[float] = Column(Float) # Note: EINs are often stored as text to preserve leading zeros
    former: Optional[str] = Column(Text)
    changed: Optional[datetime.datetime] = Column(TIMESTAMP)
    afs: Optional[str] = Column(Text)
    wksi: Optional[bool] = Column(Boolean) # Changed to Boolean and Optional
    fye: Optional[float] = Column(Float) # Note: FYE is often stored as text or a specific date type
    form: Optional[str] = Column(Text)
    period: Optional[datetime.datetime] = Column(TIMESTAMP)
    fy: Optional[float] = Column(Float) # Note: Fiscal Year is often stored as integer or text
    fp: Optional[str] = Column(Text)
    filed: Optional[datetime.datetime] = Column(TIMESTAMP)
    accepted: Optional[str] = Column(Text)
    prevrpt: Optional[bool] = Column(Boolean) # Changed to Boolean and Optional
    detail: Optional[bool] = Column(Boolean) # Changed to Boolean and Optional
    instance: Optional[str] = Column(Text)
    nciks: Optional[int] = Column(BigInteger)
    aciks: Optional[str] = Column(Text)
    pubfloatusd: Optional[float] = Column(Float)
    floatdate: Optional[datetime.datetime] = Column(TIMESTAMP)
    floataxis: Optional[float] = Column(Float)
    floatmems: Optional[float] = Column(Float)

    def __repr__(self):
        return f"<Sub(adsh='{self.adsh}', cik={self.cik}, name='{self.name}')>"


class Pre(Base):
    """
    SQLAlchemy ORM model for the 'pre' table (updated definition).
    """
    __tablename__ = 'pre'

    # Composite Primary Key (NOT NULL as per SQL)
    adsh: str = Column(Text, primary_key=True)
    report: int = Column(BigInteger, primary_key=True)
    line: int = Column(BigInteger, primary_key=True)

    # Other columns (Some are NULLable, inpth and negating are now BOOL)
    stmt: Optional[str] = Column(Text)
    inpth: Optional[bool] = Column(Boolean) # Changed to Boolean and Optional
    tag: Optional[str] = Column(Text)
    version: Optional[str] = Column(Text)
    prole: Optional[str] = Column(Text)
    plabel: Optional[str] = Column(Text)
    negating: Optional[bool] = Column(Boolean) # Changed to Boolean and Optional

    def __repr__(self):
        return (
            f"<Pre(adsh='{self.adsh}', report={self.report}, line={self.line}, "
            f"tag='{self.tag}', prole='{self.prole}', inpth={self.inpth}, negating={self.negating})>"
        )

class Num(Base):
    """
    SQLAlchemy ORM model for the 'num' table.
    """
    __tablename__ = 'num'

    # Composite Primary Key (All NOT NULL as per SQL)
    adsh: str = Column(Text, primary_key=True)
    tag: str = Column(Text, primary_key=True)
    version: str = Column(Text, primary_key=True)
    ddate: datetime.datetime = Column(TIMESTAMP(timezone=False), primary_key=True) # Assuming TIMESTAMP WITHOUT TIME ZONE
    qtrs: int = Column(BigInteger, primary_key=True)
    uom: str = Column(Text, primary_key=True)
    dimh: str = Column(Text, primary_key=True)
    iprx: int = Column(BigInteger, primary_key=True)

    # Other columns (Some are NULLable as per SQL)
    value: Optional[float] = Column(Float)
    footnote: Optional[str] = Column(Text)
    footlen: Optional[int] = Column(BigInteger)
    dimn: Optional[int] = Column(BigInteger)
    coreg: Optional[str] = Column(Text)
    durp: Optional[float] = Column(Float)
    datp: Optional[float] = Column(Float)
    dcml: Optional[int] = Column(BigInteger)

    def __repr__(self):
        # Including key parts and value in repr for easier identification
        return (
            f"<Num(adsh='{self.adsh}', tag='{self.tag}', ddate={self.ddate}, "
            f"qtrs={self.qtrs}, uom='{self.uom}', dimh='{self.dimh}', iprx={self.iprx}, "
            f"value={self.value})>"
        )

    def as_dict(self):
        return {'adsh': self.adsh, 'tag': self.tag, 'ddate': self.ddate, 'qtrs': self.qtrs, 'uom': self.uom, 'dimh': self.dimh, 'iprx': self.iprx, 'value': self.value}
