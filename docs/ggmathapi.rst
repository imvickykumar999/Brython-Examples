##################
ggMath Mathematics
##################

.. automodule:: ggame.mathapp

******************
ggMath Application
******************

MathApp
=======

.. autoclass:: MathApp

    .. autoattribute:: view_position
    .. autoattribute:: scale

    .. automethod:: getSpritesbyClass
    .. automethod:: listenKeyEvent
    .. automethod:: listenMouseEvent
    .. automethod:: unlistenKeyEvent
    .. automethod:: unlistenMouseEvent
    .. automethod:: logicalToPhysical
    .. automethod:: physicalToLogical
    .. automethod:: translateLogicalToPhysical
    .. automethod:: translatePhysicalToLogical
    .. automethod:: distance
    .. automethod:: addViewNotification
    .. automethod:: removeViewNotification
    .. automethod:: run

ggMath Base Class for Visual Objects
====================================

.. autoclass:: _MathVisual
    :members:


.. automodule:: ggame.point

*************
Point Objects
*************

These classes are subclasses of :class:`~ggame.sprite.Sprite` and are used
to represent points in geometry and mathematics.

_Point
======

This is the abstract base class for all point classes.

.. autoclass:: _Point
    :members:

Point
=====

.. autoclass:: Point
    :members:


ImagePoint
==========

.. autoclass:: ImagePoint
    :members:


.. automodule:: ggame.line

************
Line Objects
************

This category currently only has one class: :class:`LineSegment`, but will
eventually be extended to include at least :class:`Line` and :class:`Ray`.

LineSegment
===========

.. autoclass:: LineSegment
    :members:

Circle
======

.. automodule:: ggame.circle

.. autoclass:: Circle
    :members:

************
Text Objects
************

Label
=====

.. automodule:: ggame.label

.. autoclass:: Label
    :members:

**********
Indicators
**********

.. automodule:: ggame.indicator

ImageIndicator
==============

.. autoclass:: ImageIndicator
    :members:

LEDIndicator
============

.. autoclass:: LEDIndicator
    :members:

**************
Input Controls
**************

Slider
======

.. automodule:: ggame.slider

.. autoclass:: Slider
    :members:

InputNumeric
============

.. automodule:: ggame.input

.. autoclass:: InputNumeric
    :members:

InputButton
===========

.. autoclass:: InputButton
    :members:

.. automodule:: ggame.inputpoint

InputImageButton
================

.. autoclass:: InputImageButton
    :members:

InputImageToggle
================

.. autoclass:: InputImageToggle
    :members:

MetalToggle
===========

.. autoclass:: MetalToggle
    :members:

GlassButton
===========

.. autoclass:: GlassButton
    :members:

************
Time Utility
************

.. automodule:: ggame.timer

Timer
=====

.. autoclass:: Timer
    :members:



